import { useState } from "react";
import api from "../services/api";

export default function UploadZone({
  setPolicyData,
  setSummary,
}) {
  const [loading, setLoading] = useState(false);

  const handleUpload = async (event) => {
    const file = event.target.files[0];

    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);

      const uploadResponse =
        await api.post(
          "/upload-policy",
          formData,
          {
            headers: {
              "Content-Type":
                "multipart/form-data",
            },
          }
        );

      setPolicyData(uploadResponse.data);

      const summaryForm = new FormData();
      summaryForm.append("file", file);

      const summaryResponse =
         await api.post(
           "/summarize-policy",
           summaryForm,
          {
            headers: {
              "Content-Type": "multipart/form-data",
           },
        }
      ); 
    console.log("Summary Response:", summaryResponse.data);  

    setSummary(summaryResponse.data.summary);

    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-white border border-gray-200 rounded-2xl p-8">
      <h2 className="text-2xl font-bold mb-4">
        Upload Policy
      </h2>

      <div className="border-2 border-dashed border-blue-300 rounded-xl p-12 text-center">
        <input
          type="file"
          accept=".pdf"
          onChange={handleUpload}
        />

        {loading && (
          <div className="mt-6 text-blue-600 font-medium">
            Analyzing Policy...
          </div>
        )}
      </div>
    </div>
  );
}